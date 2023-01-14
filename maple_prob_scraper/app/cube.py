import json
import os
from pathlib import Path
from maple_prob_scraper.converter.cube import get_cube_detail
from maple_prob_scraper.resource.cube import CubeId, Grade, PartType
from maple_prob_scraper.type.cube_detail import CubeDetail


class CubeApp:
    cube_id = CubeId.suspicious_cube
    cube_grade = Grade.rare
    must_part = [
        PartType.weapon,
        PartType.cap,
        PartType.coat,
        PartType.pants,
        PartType.gloves,
        PartType.shoes,
        PartType.faceAccessory,
    ]
    default_req_level = 120
    item_options = {}

    def init_item_options(self):
        if len(self.item_options) == 0:
            with open(Path(os.path.dirname(__file__)).parent / "resource" / "item-option.json", "r") as f:
                self.item_options = json.load(f)

        return self.item_options


    def run(self) -> list[CubeDetail]:
        if self.cube_id == CubeId.suspicious_cube:
            if self.cube_grade in [Grade.unique, Grade.legendary]:
                raise ValueError()
        elif self.cube_id == CubeId.craftmans_cube:
            if self.cube_grade in [Grade.legendary]:
                raise ValueError()

        self.init_item_options()

        details = self.get_detail_list()
        weights = self.convert_value_to_weight(details)
        code_weights = self.convert_key_to_code(weights)
        return code_weights

    def get_detail_list(self) -> list[CubeDetail]:
        details = []
        for part in self.must_part:
            details.append(
                get_cube_detail(
                    self.cube_id,
                    self.cube_grade,
                    part,
                    self.default_req_level
                )
            )

        return details

    def probs_to_weight(self, data: dict[str, float]) -> dict[str, int]:
        prob_sum = 0
        for prob in data.values():
            prob_sum += prob

        weight_sum = 0
        for try_weight_sum in range(1, 1000):
            ok = True
            for prob in data.values():
                if not round(prob / prob_sum * try_weight_sum, 3).is_integer():
                    ok = False
                    break
            if ok:
                weight_sum = try_weight_sum
                break
        if weight_sum == 0:
            raise ValueError()

        result = {}
        for key, prob in data.items():
            result[key] = round(prob / prob_sum * weight_sum, 3)

        return result

    def convert_value_to_weight(self, details: list[CubeDetail]) -> dict[str, int]:
        weights_list = []
        for detail in details:
            probs = self._prob_str_to_float(detail.probs)
            weights_list.append(self.probs_to_weight(probs))

        result = {}
        for weights in weights_list:
            for key, weight in weights.items():
                if key in result:
                    if result[key] != weight:
                        raise ValueError("Different weights")
                result[key] = weight

        return result

    def convert_key_to_code(self, weights: dict[str, int]) -> dict[int, int]:
        selected = {}
        is_additional = self.cube_id in [CubeId.additional_cube]
        for code, data in self.item_options.items():
            code = int(code)
            if code // 10000 != self.cube_grade.value:
                continue
            if (
                code // 1000 % 10 == 0 and is_additional or
                code // 1000 % 10 == 2 and not is_additional
            ):
                continue
            selected[code] = self._convert_summary(data['string'], data['level'], self.default_req_level)

        result = {}
        for key, weight in weights.items():
            for code, summary in selected.items():
                if summary == key:
                    result[code] = weight
                    break
        return result

    def _prob_str_to_float(self, probs: dict[str, str]) -> dict[str, float]:
        result = {}
        for key, prob_str in probs.items():
            if prob_str.endswith('%'):
                prob_str = prob_str[:-1]
            result[key] = float(prob_str)
        return result

    def _convert_summary(self, summary: str, levels: dict, req_level: int) -> str:
        level = levels[str(self._get_option_level(req_level))]
        level_sorted = sorted(level.keys(), key=lambda s: len(s))
        for key in level_sorted:
            value = level[key]
            summary = summary.replace('#' + key, str(value))
        summary = summary.replace(',', '')
        return summary

    def _get_option_level(self, req_level: int) -> int:
        if req_level <= 0:
            return 1
        elif req_level >= 250:
            return 25
        else:
            return (req_level + 9) // 10
