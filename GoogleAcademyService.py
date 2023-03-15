from scholarly import scholarly


# search by name in Google Academy
def searchByAuthorName(name):
    try:
        search_query = scholarly.search_author(name)
        first_author_result = next(search_query)
        author = scholarly.fill(first_author_result)
        return {"name": author["name"], "hindex": author["hindex"], "i10index": author["i10index"],
                "imgUrl": author["url_picture"], "resource": "GoogleAcademy"}
    except Exception as e:
        print(e)


def findByAuthorID(authorID):
    # TODO findByAuthorID
    print()


def findAuthorsByCountryId(countryId):
    # TODO findByCountryId
    print()


def findAuthorsWithPublications():
    # TODO find authors with publications
    print()
