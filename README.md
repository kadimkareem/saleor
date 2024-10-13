 
**Saleor Repo Issues Analysis**

## How to Run



<be>
<be>


1. **GitHub Access Token**
The project contains an-issues dataset file fetched from GitHub on October 10, 2024. It requires an access token to obtain the issues data. I have already added mine, but if you need to fetch the latest data, you will have to use the GitHub API. To do this, you will need to obtain an "Access Token."

   to do this    
   - Visit [GitHub Personal Access Tokens](https://github.com/settings/tokens) and generate a new token with the necessary permissions (at     least read access to repository issues).
   - Save this token in a file called `access_token.json` in the root of your project directory. The file should look like this:

   ```json {"access_token": "your_github_token_here"}```



<be>
<be>
2. **Install Python**:

 Ensure Python is installed on your machine. You can download and install it from [python.org](https://www.python.org/downloads/).
 





3. **[Optional] Create a virtual environment**: 
 
It’s recommended to create a virtual environment to keep your dependencies isolated. You can do this with the following command:
   ```bash python -m venv env ```
   
activate the virtual environment:
on windows  ```bash .\env\Scripts\activate```
on mac ```bash source env/bin/activate ```






4.	**Install Requirements:**


    Install the necessary dependencies from the requirements.txt file by running

   ```bash pip install -r requirements.txt```





5.	**You can run any of the scripts in the terminal with:**

```bash python scriptname.py```

    
