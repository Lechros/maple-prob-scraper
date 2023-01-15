from maple_prob_scraper.resource.cube import CubeId, Grade
from maple_prob_scraper.type.cube_detail import CubeDetail
from maple_prob_scraper.app.cube import CubeApp

if __name__ == "__main__":
    capp = CubeApp()
    capp.cube_id = CubeId.meisters_cube

    for grade in [Grade.rare, Grade.epic, Grade.unique, Grade.legendary]:
        capp.cube_grade = grade

        result = capp.run()

        print('Cube:', capp.cube_id)
        print('Grade:', capp.cube_grade)
        for code, weight in result.items():
            print(f'{code}\t{weight}')
