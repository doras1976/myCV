from flask import Flask, render_template

app = Flask(__name__)

# CV data to be used across pages
cv_data = {
    'name': 'Dora Schreiber',
    'contact': {
        'phone': '054-2537333',
        'email': 'doritsrbr@gmail.com',
        'linkedin': 'https://www.linkedin.com/in/dora-schreiber/'
    },
    'summary': (
        "Experienced and enthusiastic Automation infrastructure developer, "
        "leading complex tasks side-by-side with developers and product owners, "
        "striving to deliver end-to-end use-cases. Experienced working in an "
        "Agile/Scrum development framework. Strong ability and desire to quickly "
        "self-learn new technologies and tools and apply them for the team’s benefit "
        "while increasing team productivity. I'm also a longevity freak, an amateur "
        "road cyclist, and a chess player."
    ),
    'experience': [
        {
            'period': '2022 - now',
            'position': 'Automation Engineer',
            'company': 'Rapyd',
            'details': [
                'Python Automation oriented developer in the fintech field',
                'Infrastructure and tests development in Python, using REST API in an OOP environment'
            ]
        },
        {
            'period': '2021- 2022',
            'position': 'Automation Engineer',
            'company': 'Sealights',
            'details': [
                'TypeScript Automation oriented developer in the test optimization field',
                'Infrastructure and tests development in TypeScript, using REST API in an OOP environment'
            ]
        },
        {
            'period': '2021',
            'position': 'Automation Engineer',
            'company': 'Amicus.io',
            'details': [
                'Python Automation oriented developer in the fintech field',
                'Infrastructure and tests development in Python, using REST API in an OOP environment'
            ]
        },
        {
            'period': '2018 – 2020',
            'position': 'Automation Engineer',
            'company': 'Avaya',
            'details': [
                'Leader of QA Automation process of an on-premise video conferencing management solution.',
                'Experienced with automation infrastructure development in Python, using Selenium, REST API and Robot Framework as a keyword-driven testing framework.',
                'Experienced working in an Agile/Scrum development framework, using Git and Bamboo for CI/CD purposes: building the product version, running the automated tests, and getting results in the shortest time.',
                'Results and logs analysis, high-quality bugs opening and their management via Jira.',
                'Handling a variety of test types: Regression, Sanity, Load, Stress, etc.'
            ]
        },
        {
            'period': '2013 – 2018',
            'position': 'Automated QA Tester',
            'company': 'Avaya',
            'details': [
                'Designing and writing tests using already written actions and keywords with TestNG and proprietary tools.',
                'Running the tests, analyzing test results and logs, opening and managing bugs.'
            ]
        },
        {
            'period': '2008 – 2013',
            'position': 'QA Engineer',
            'company': 'Radvision',
            'details': [
                'Test documents designing and writing using Quality Center.',
                'Functional and interoperability testing of the company products.',
                'Analyzing test results and logs, opening and managing bugs.'
            ]
        },
        {
            'period': '2005 – 2008',
            'position': 'QA Engineer',
            'company': 'VocalTech',
            'details': [
                'Test documents designing and writing.',
                'Functional testing of the company products.',
                'Analyzing test results and logs, opening and managing bugs.'
            ]
        },
        {
            'period': '2002 – 2005',
            'position': 'Tax Law Office',
            'company': '',
            'details': [
                'Managing the office internet site.'
            ]
        }
    ],
    'education': [
        '2019: Python (Coursera University of Michigan Specialization)',
        'Professional Scrum Master I (Scrum.org)',
        '2008: ISTQB (Foundation Certificate in Software Testing)',
        '2001: Graduated B.Sc., Software Engineering, HIT'
    ],
    'military_service': '1995 – 1997: Applications instructor, computers department (Mamram graduate)',
    'skills': [
        'Automation-oriented development in Python, Selenium, Robot Framework, TypeScript, Cypress.',
        'Linux, VMware, Docker Container, Bamboo, Git, Jira, Jenkins'
    ],
    'languages': [
        'Hebrew: Native Speaker',
        'English: Proficient'
    ]
}

@app.route('/')
def home():
    return render_template('home.html', cv=cv_data)

@app.route('/experience')
def experience():
    return render_template('experience.html', cv=cv_data)

@app.route('/personal')
def personal():
    return render_template('personal.html', cv=cv_data)

if __name__ == '__main__':
    app.run(debug=True)
