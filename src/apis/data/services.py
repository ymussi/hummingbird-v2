from models import City
from sqlalchemy.sql import or_

class ReportService():
    
    def getAllCityCases(self):
        todos_casos = City.query.all()

        return compileCases(todos_casos)

    def searchCityCasesByState(self, sigla):
        situacao_cidades = City.query.filter_by(
            state=sigla).all()

        return compileCases(situacao_cidades)



def compileCases(dados):
    activeCases = sum([(cidade.total_cases - cidade.suspects - cidade.refuses -
                    cidade.deaths - cidade.recovered) for cidade in dados]) or 0
    suspectedCases = sum(
        [cidade.suspects for cidade in dados]) or 0
    recoveredCases = sum(
        [cidade.recovered for cidade in dados]) or 0
    deaths = sum([cidade.deaths for cidade in dados]) or 0

    return {
        'activeCases': activeCases,
        'suspectedCases': suspectedCases,
        'recoveredCases': recoveredCases,
        'deaths': deaths
    }