from datetime import datetime, timedelta
import openpyxl
import requests


def download_file():
    url = 'http://www.icsi.edu/Docs/Webmodules/Requirement.xlsx'
    local_filename = '/tmp/' + url.split('/')[-1]
    print('Downloading File...', local_filename)
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print('Downloaded')
    return local_filename


def str_to_date(s):
    if s.startswith('Reposted on '):
        dt = datetime.strptime(
            s.replace('Reposted on ', ''), '%d-%m-%Y').date()
        print('dt', dt)
        return dt
    elif s.startswith('Re posted on '):
        dt = datetime.strptime(
            s.replace('Re posted on ', ''), '%d-%m-%Y').date()
        print('dt', dt)
        return dt
    elif s.startswith('Re-posted on '):
        dt = datetime.strptime(
            s.replace('Re-posted on ', ''), '%d-%m-%Y').date()
        print('dt', dt)
        return dt
    else:
        # todo - email to me
        return datetime.strptime(s, '%d/%m/%Y').date()


def max_row(sheet):
    h_column = sheet['H']
    max_col = 2
    now = datetime.now() - timedelta(days=7)
    for col in h_column[2:20]:
        d = col.value

        if isinstance(d, datetime) and d.date() >= now.date():
            max_col += 1
        elif isinstance(d, str) and str_to_date(d) and str_to_date(d) >= now.date():
            max_col += 1
        else:
            print(max_col)
            break

    return max_col


def post_to_cs_trainee(row):
    """
    S.No.
    Company Name
    Address
    Email id
    Contact Person Name
    Requirement
    Location
    Posted on
    """
    d = row[7].value
    if isinstance(d, datetime):
        url = 'https://forum.csclub.co/posts'
        payload = {
            "api_key": "ef759d736fc5495f16fd29eef742e822cd1203c81a9e871eef863b3dc10aad2f",
            "api_username": "vaibhavmule",
            "title": "{} Looking for CS Trainees in {}".format(
                row[1].value, row[6].value),
            "raw": "**Company Name:** {} \n**Requirement:** {} \n**Address:** {} \n**Location:** {} \n**Email:** {} \n**Contact Person:** {} \n\n **Source:** {} at [ICSI](https://www.icsi.edu/Docs/Webmodules/Requirement.xlsx) \n\n\n **Recommended Reading:** \n https://forum.csclub.co/t/5-things-you-need-to-know-about-cs-training-cs-club/1032?u=vaibhavmule".format(
                row[1].value,
                row[5].value,
                row[2].value,
                row[6].value,
                row[3].value,
                row[4].value,
                row[7].value.strftime('%m/%d/%Y'),),
            "category": 6,  # cs trainees category
            "tags": ["".join(row[6].value.split()).lower()],
            "tags": [],
        }
        # print(payload["row"])
        print('----------------------------------------\n')
        print("{} Looking for CS Trainees in {}".format(
            row[1].value, row[6].value),)
        print("<strong>Company Name:</strong> {} <br/><strong>Requirement:</strong> {} <br/><strong>Address:</strong> {} <br/><strong>Location:</strong> {} <br/><strong>Email:</strong> {} <br/><strong>Contact Person:</strong> {} <br/><br/> <strong>Source:</strong> {} at <a href='https://www.icsi.edu/Docs/Webmodules/Requirement.xlsx'>ICSI</a>".format(
            row[1].value,
            row[5].value,
            row[2].value,
            row[6].value,
            row[3].value,
            row[4].value,
            row[7].value.strftime('%m/%d/%Y')))
    else:
        print('----------------------------------------\n')
        print("{} Looking for CS Trainees in {}".format(
            row[1].value, row[6].value),)
        print("<strong>Company Name:</strong> {} <br/><strong>Requirement:</strong> {} <br/><strong>Address:</strong> {} <br/><strong>Location:</strong> {} <br/><strong>Email:</strong> {} <br/><strong>Contact Person:</strong> {} <br/><br/> <strong>Source:</strong> {} at <a href='https://www.icsi.edu/Docs/Webmodules/Requirement.xlsx'>ICSI</a>".format(
            row[1].value,
            row[5].value,
            row[2].value,
            row[6].value,
            row[3].value,
            row[4].value,
            row[7].value))
        # r = requests.post(url, data=payload)
        # print('response', r.text, r.status_code)


def main():
    file_path = download_file()
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    mx_row = max_row(sheet)
    print(mx_row)
    if mx_row > 2:
        for row in sheet.iter_rows(min_row=3, max_col=8, max_row=mx_row):
            post_to_cs_trainee(tuple(row))


main()
