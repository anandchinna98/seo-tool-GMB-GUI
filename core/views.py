from .models import Sites, create_record


def add_record(name, url, keyword,cities):
    site = Sites(
        name=name,
        url=url,
        keywords=keyword,
        cities=cities,
    )
    create_record(site)

if __name__ =="__main__":
    def add_record(name, url, keyword,cities):
        site = Sites(
            name="desss",
            url="www.desss.com",
            keywords="design,development,deployment",
            cities="chennai, cuddalore,panruti",
        )
        create_record(site)
