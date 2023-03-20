from setuptools import find_packages ,setup


REQUIREMENT_FILE_NAME = "requirements.txt"
def get_requirement()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list =[requrement_name.replace("\n","") for requirement_name in requirement_list]

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list




setup(
    name= "senor",
    author = "JatinKumarMahaldar",
    version="0.0.1",
    author_email="jatinkumarmahaldar@gmail.com",
    packages= find_packages(),
    install_requires= get_requirement(),
)