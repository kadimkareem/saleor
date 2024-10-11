
from typing import List
from issue_model import Issue
from statistic import model_from_json


issues:List[Issue]= model_from_json()



def main():
    print(issues)
if __name__=="__main__":
    main()