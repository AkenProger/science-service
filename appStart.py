from flask import Flask, render_template, request
import GoogleAcademyService
import DBHelper

app = Flask(__name__)


@app.route("/")
def index_page():
    dataPage = DBHelper.select_all_authors()
    return render_template("index.html", datas=dataPage)


@app.route("/searchName/")
def searchName():
    author_name = request.args.get("name")
    data = GoogleAcademyService.searchByAuthorName(author_name.strip())

    if data is None:
        return render_template("error.html", message="Автор не найден!")

    dataToSave = (data["name"], data["hindex"], data["i10index"], data["imgUrl"], data["resource"])

    duplicateChecker = DBHelper.select_all_authors()
    for i in duplicateChecker:
        if str(i[2]) == data["name"]:
            dataForUpdate = (data["hindex"], data["i10index"], data["imgUrl"], i[0])
            DBHelper.updateAuthor(dataForUpdate)
            return render_template("error.html", message="Автор уже существует в нашей базе данных! ДАННЫЕ "
                                                         "СИНХРОНИЗИРОВАНЫ")

    DBHelper.createAuthor(dataToSave)
    return render_template("result.html", data=data)


@app.route("/filter/")
def filterAuthors():
    filterKey = request.args.get("select")
    match filterKey:
        case "hindex":
            dataH = DBHelper.filterAuthors(filterKey)
            print(dataH)
            return render_template("index.html", datas=dataH, sess1="selected")
        case "i10index":
            dataI = DBHelper.filterAuthors(filterKey)
            return render_template("index.html", datas=dataI, sess2="selected")
        case _:
            return render_template("index.html", filterErr="Не правильный фильтр")
