def Display(request):
    with open('mi_vs_csk.csv', 'r') as data:
        csv_reader = csv.reader(data)
        data1 = list(csv_reader)
    context = {
        "data" : data1,
    }
    return render(request, "template.html", context)