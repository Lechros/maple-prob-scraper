from typing import Optional
from bs4 import BeautifulSoup
from maple_prob_scraper.resource.cube import CubeId, Grade, PartType

from maple_prob_scraper.type.cube_detail import CubeDetail
from maple_prob_scraper.request import get


def fetch_prob(cube_id: CubeId, grade: Grade, part: PartType, req_lev: int) -> str:
    data = {
        'nCubeItemID': cube_id.value,
        'nGrade': grade.value,
        'nPartsType': part.value,
        'nReqLev': req_lev
    }
    return get('/Guide/OtherProbability/cube/GetSearchProbList', data).text


def parse_prob(html: str) -> dict[str, str]:
    probs = {}
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find('table', { 'class': ['cube_data', '_1'] }).find('tbody').find_all('tr')
    for row in rows:
        tds = row.find_all('td')
        name = tds[0].text
        prob = tds[1].text
        probs[name] = prob
    return probs


def get_cube_detail(
    cube_id: CubeId,
    grade: Grade,
    part: PartType,
    req_lev: int,
    html: Optional[str] = None
) -> CubeDetail:
    if html is None:
        html = fetch_prob(cube_id, grade, part, req_lev)

    detail = CubeDetail()
    detail.cube_id = cube_id
    detail.cube_grade = grade
    detail.part_type = part
    detail.req_level = req_lev
    detail.probs = parse_prob(html)

    return detail