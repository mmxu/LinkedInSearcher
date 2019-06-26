from linkedin_searcher.dals.userdatabase import UserDatabase
from linkedin_searcher.searcher import LinkedInSearcher
from api.app import SearcherApiServer

database = UserDatabase('sqlite+pysqlite:///users.db')
searcher = LinkedInSearcher(database)
api_server = SearcherApiServer(searcher)
api_server.run()