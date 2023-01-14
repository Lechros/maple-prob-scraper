import requests
from bs4 import BeautifulSoup

from maple_prob_scraper.cube.cube_detail import CubeDetail


def get_cube_detail(cube_id: int, grade: str, part: str, req_lev: int) -> CubeDetail:
    url = 'https://maplestory.nexon.com/Guide/OtherProbability/cube/GetSearchProbList'
    header = {
        "Connection": "keep-alive",
        "X-Requested-With": "XMLHttpRequest",
    }
    data = {
        'nCubeItemID': cube_id,
        'nGrade': grade,
        'nPartsType': part,
        'nReqLev': req_lev
    }
    detail = CubeDetail()
    detail.cube_id = cube_id
    detail.cube_grade = grade
    detail.part_name = part
    detail.req_lev = req_lev
    res = requests.post(url=url, data=data, headers=header)
    soup = BeautifulSoup(res.text, 'html.parser')
    rows = soup.find('table', { 'class': ['cube_data', '_1'] }).find('tbody').find_all('tr')
    for row in rows:
        tds = row.find_all('td')
        name = tds[0].text
        prob = tds[1].text
        detail.probs[name] = prob
    return detail
