from bs4 import BeautifulSoup
from sys import exit

file_name = "autoescuela/aeol_data.html"
test_record = {}


with open(file_name, "r") as f:
    doc = BeautifulSoup(f, "html.parser")
    tests = doc.find("div", {"class": "tests_grid"}).find_all("div")

def save_tests():
    for test in tests:
        try:
            test_record.update({tests.index(test) + 1: int(test.get("title").split()[5])})
        except:
            pass
    return test_record

def average_mistakes():
    total_mistakes = 0
    for test in test_record:
        i = int(test_record.get(test))
        total_mistakes = total_mistakes + i

    average = total_mistakes / len(test_record)
    average_perct = average/30 * 100
    return round(average, 2), round(average_perct, 2)

def test_results():
    results = {"Impecable": 0, "% Impecable": 0, "Aprobado": 0, "% Aprobado": 0, "Suspenso": 0, "% Suspenso": 0, "Superado": 0,"% Superado": 0}
    for test in test_record:
        result = test_record.get(test)
        if result == 0:
            results.update({"Impecable": results.get("Impecable") + 1})
        elif result > 0 and result <= 3:
            results.update({"Aprobado": results.get("Aprobado") + 1})
        elif result > 3:
            results.update({"Suspenso": results.get("Suspenso") + 1})

    results.update({"% Impecable": round(results.get("Impecable") / len(test_record) * 100, 2)})
    results.update({"% Aprobado": round(results.get("Aprobado") / len(test_record) * 100, 2)})
    results.update({"% Suspenso": round(results.get("Suspenso") / len(test_record) * 100, 2)})
    results.update({"Superado": len(test_record) - round(results.get("Suspenso"))})
    results.update({"% Superado": 100 - results.get("% Suspenso")})
    return results

def show_graph():
    print("\n\nESTE ES EL GRÁFICO DE TUS TESTS:\n")
    for test in test_record.keys():
        mistakes = test_record.get(test) 
        print(f"[{test}] {"□" * mistakes * 5 if mistakes <= 3 else "■" * mistakes * 5} - {mistakes} fallos")

def show_stats():
    results = test_results()
    print("\nEstas son tus estadísticas en la teórica del permiso B:")
    print(f"\nExamenes totales: {len(test_record)}\nDe los cuales:\nSuperados: {results.get("Superado")} -> {results.get("% Superado")}%")
    print(f"\nImpecables: {results.get("Impecable")} -> {results.get("% Impecable")}%\nAprobados: {results.get("Aprobado")} -> {results.get("% Aprobado")}%\nSuspensos: {results.get("Suspenso")} -> {results.get("% Suspenso")}%")

    print(f"\n\nRespecto a los fallos:\n\nLa media de fallos por test es de: {average_mistakes()[0]} -> {average_mistakes()[1]}%")
    print(f"Esta media es de {'APROBADO, < 10% (3 fallos)' if average_mistakes()[0] <= 3 else "SUSPENSO, > 10% (+3 fallos)"}")

    action = input("\nQuieres ver el gráfico de tus tests? (s/n): ")

    match action:
        case 's':
            show_graph()
        case _:
            exit_app()

def exit_app():
    print("¡Hasta pronto, no te olvides de estudiar!")
    exit()

def main():
    action = input("\nQuieres ver las estadísticas de tus tests para el permiso B? (s/n): ")

    match action:
        case 's':
            show_stats()
        case 'n':
            exit_app()
        case '':
            exit_app()
        case _:
            print('Wrong input, try again.')
            main()

if __name__ == "__main__":
    save_tests()
    main()
