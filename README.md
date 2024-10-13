 
**Saleor Repo Issues Analysis**

## How to Run



1. **GitHub Access Token**:
   
   To interact with GitHub's API, you need a GitHub access token. Follow these steps to create one:
   
   - Visit [GitHub Personal Access Tokens](https://github.com/settings/tokens) and generate a new token with the necessary permissions (at least read access to repository issues).
   - Save this token in a file called `access_token.json` in the root of your project directory. The file should look like this:

   ```json {
      "access_token": "your_github_token_here"
   }```

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

    
