# Install and Auth Quickstart
If you are a python beginner, please head to our [more in depth guide](getting_started_for_python_beginners.md) where we walk through creating a python virtual environment before installing prefect.

## 1. [Log into Cloud from your browser](https://app.prefect.cloud/)
Much of Prefect's functionality is backed by an API. Sign up for a forever free Prefect Cloud account or accept your organization's invite to join their Prefect Cloud account. Head to [https://app.prefect.cloud/](https://app.prefect.cloud/) to login to Prefect Cloud's UI from your web browser.

TODO: talk to w about this

IF your company has already set up SSO, please click `Sign in with SSO` to avoid creating a duplicate account.

<img src="images/sso_login_button.png" width="300"/>

## 2. [Log in to Cloud](https://docs.prefect.io/latest/cloud/connecting/#log-into-prefect-cloud-from-a-terminal) from a terminal
Log into prefect cloud from your terminal so that you can author flows.

```bash
prefect cloud login
```
Select **Log in with a web browser**
![Alt text](images/login_with_wbrowser.png)

#### Alternatively, manually login with API key

<img src="images/get_api_key.png" width="300"/>

Find trouble shooting tips for login errors [here](https://docs.prefect.io/latest/cloud/connecting/#prefect-cloud-login-errors)!


## 3. [Change Workspaces](https://docs.prefect.io/latest/cloud/connecting/#change-workspaces) to your workspace of choice
```bash
prefect cloud workspace set
```
Then select the desired workspace from list.

## (Optional) [Prefect Profiles](https://docs.prefect.io/latest/guides/settings/#configuration-profiles)
Prefect allows you to persist settings instead of setting an environment variable each time you open a new shell. Settings are persisted to profiles, which allow you to move between groups of settings quickly.

To create a profile:
```bash
prefect profile create test
```

To switch to a selected profile:
```bash
prefect profile use test
```

Profiles are stored by default in your PREFECT_HOME directory:
```bash
vim ~/.prefect/profiles.toml
```

Example `profiles.toml` file:

```toml
active = "default"

[profiles.local]
PREFECT_API_URL = "http://127.0.0.1:4200/api"

[profiles.default]
PREFECT_API_KEY = "pnu_----replace-me----"
PREFECT_API_URL = "https://api.prefect.cloud/api/accounts/--replace-me--/workspaces/--replace-me--"

[profiles.staging]
PREFECT_API_KEY = "pnu_----replace-me----"
PREFECT_API_URL = "https://api.prefect.cloud/api/accounts/--replace-me--/workspaces/--staging-workspace-replace-me--"
PREFECT_LOGGING_LEVEL = "DEBUG"

[profiles.n]
PREFECT_API_KEY = "pnu_----replace-me----"
PREFECT_API_URL = "https://api.prefect.cloud/api/accounts/--replace-me--/workspaces/--n-workspace-replace-me--"
```
