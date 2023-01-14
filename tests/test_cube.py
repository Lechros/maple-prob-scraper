from maple_prob_scraper.converter.cube import get_cube_detail
from maple_prob_scraper.type.cube_detail import CubeDetail


def test_get_cube_detail():
    detail: CubeDetail = get_cube_detail(5062009, '에픽', '모자', 120)

    assert detail.cube_id == 5062009
    assert detail.cube_grade == '에픽'
    assert detail.part_name == '모자'
    assert detail.req_level == 120
    assert len(detail.probs) > 0