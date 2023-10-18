from retriever import Retriever
from processor import Processor
from alerter import Alerter


def main():
    url = "http://www.volonte-d.com/perso/paille.php"

    retriever_instance = Retriever(url=url)
    ps = retriever_instance.get_page_source()

    processor_instance = Processor(text=ps)
    divs_crew_names = processor_instance.extract_crew_names()

    Alerter.alert("\n".join(divs_crew_names))

    print(divs_crew_names)


if __name__ == "__main__":
    main()
