import datetime
import pytz
import os

# def get_current_time():
#     return datetime.datetime.now(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S UTC')

def get_current_time_ist():
    utc_time = datetime.datetime.now(pytz.UTC)
    ist_time = utc_time.astimezone(pytz.timezone('Asia/Kolkata'))
    return ist_time.strftime('%Y-%m-%d %H:%M:%S IST')

def generate_readme():
    template = f'''
<div align="right">
<sub>Last sync: {get_current_time_ist()}</sub>
</div>'''
    return template
def main():
    readme_content = generate_readme()
    with open('README.md', 'w') as f:
        f.write(readme_content)
if __name__ == "__main__":
    main()
