# running-duck
running duck builds you a running plan based upon your level, race distance, and race date. 
Simply set your parameters in `duck_run.py` and go.



<img width="433" alt="Screenshot 2025-01-02 at 10 00 48 AM" src="https://github.com/user-attachments/assets/aa61195a-9589-4479-80fb-246387a997a2" />

## How does it know?
For 5k, 10k, Halfs and Marathons the data is pulled from [80/20 Running's appendix](https://www.amazon.com/80-20-Running-Stronger-Training/dp/0451470885). It's a great read you data nerds. If you want to download just the appendix its [here](https://d2fahduf2624mg.cloudfront.net/pre_purchase_docs/BK_TANT_007549/2020-06-25-05-08-30/bk_tant_007549.pdf).

For the Ultra Marathon I spliced [relentlessforwardcommotion](https://relentlessforwardcommotion.com/free-50-mile-ultramarathon-training-plan-guide/) 's plan with 80/20 Running's appendix. I lined up compreable runs between the two and added b2b runs (aka back to back run days)

## Setup
1. Read the book 80/20 Running by Matt Fitzgerald. If you don't read the book you won't understand running descriptions and methodology.
2. Create a [virtual python environment](https://github.com/pyenv/pyenv) and activate it.
3. Install duckdb `pip install duckdb`

## Set your parameters
You will need to set your parameters in in `duck_run.py`
```
input_race_distance = 'Ultra Marathon'    # choose '5k' '10k', 'Half Marathon', 'Marathon', 'Ultra Marathon'
input_training_level = 1                  # choose 1,2,3
input_race_date = '2025-07-26'            # Input your race date YYYY-MM-DD
```

## Export to Google
This script creates a csv file that you can [upload to your Google Calendar](https://support.google.com/calendar/answer/37118?hl=en&co=GENIE.Platform%3DDesktop#zippy=)
When importing I highly suggest creating a new calendar first in Google Calendar. This way if you mess up, or have to move your race dates you can just create a new calendar. Adding 150 events to a shared calendar with your spouse is highly discouraged. They don't like that.

## Example 
<img width="1199" alt="Screenshot 2025-01-02 at 10 25 20 AM" src="https://github.com/user-attachments/assets/ba7477ea-3710-49b4-84cb-15e6684aedd9" />
