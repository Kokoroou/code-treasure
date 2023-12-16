from random import randint, choice
import pandas as pd
from faker import Faker
from tqdm import tqdm


def generate_id_card():
    province_id = "{:0>3}".format(str(randint(1, 96)))
    gender_id = str(randint(0, 3))
    year_id = "{:0>2}".format(str(randint(0, 90)))
    random_id = "{:0>6}".format(str(randint(0, 999999)))

    new_id = province_id + gender_id + year_id + random_id
    return new_id


def generate_email():
    domain_list = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "msn.com", "live.com"]
    domain = choice(domain_list)

    fake = Faker()
    name = []

    while len(name) != 2:
        new_name = fake.name()
        name = new_name.split()

    first_name, last_name = name

    email_address_1 = first_name.lower() + "." + last_name.lower() + "@" + domain
    email_address_2 = fake.email()
    email_address_3 = "{}{:0>2}{:0>2}@{}".format(first_name.lower(), str(randint(1, 31)), str(randint(1, 12)), domain)

    email_address = choice([email_address_1, email_address_2, email_address_3])
    return email_address


if __name__ == "__main__":
    df = pd.read_csv("./Loan.csv")
    df = df.sort_values(by=['userId'])

    new_order = ['userId', 'age', 'job',
                 'thresholds', 'Approval Rate', 'Rejection Rate', 'N Approved', 'N Rejected',
                 'rawPrediction', 'probability',
                 'Score', 'label', 'prediction',
                 ]

    df = df[new_order]
    print(df.head())

    email = []
    idCard = []

    for userId in tqdm(list(range(len(df.index)))):
        idCard.append(generate_id_card())
        email.append(generate_email())

    df["email"] = email
    df["idCard"] = idCard

    df.to_csv("./NewLoan.csv", index=False)

    print(df.head())
