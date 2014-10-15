django-fixtures-json2csv
========================

Convert Django JSON fixtures to CSV.

**Motivation**

I'm not found good tools for convertation from django fixtures formats(json, xml, yaml)
to CSV with auto detecting of fields of django models.

**Requiremets**

Python3 

__***WARNING***__

Primary keys for Django models('pk') are saved in column with name 'id'.

**Usage**

<pre>
$ python3 json2csv.py -h 
usage: json2csv.py [-h] -i FILE -o FILE [-lf FILE] [-lv LOG LEVEL]
                   [-ex EXCLUDE FIELDS]

Convert django fixtures(JSON) to CSV

optional arguments:
  -h, --help            show this help message and exit
  -i FILE, --input-file FILE
                        Input file path
  -o FILE, --output-file FILE
                        Output file path
  -lf FILE, --log-file FILE
                        Log file path
  -lv LOG LEVEL, --log-level LOG LEVEL
                        Log level, default: INFO
  -ex EXCLUDE FIELDS, --exclude-fields EXCLUDE FIELDS
                        Log level, format: "title,name,doc"
</pre>

**Examples**

1) Use all found fields:

Input file(raw output of 'django dumpdata myapp.model' without any pretty formatting): 
<pre> 
$ cat /tmp/JobType-2014-10-14.json 
[{"pk": 1, "model": "sport.jobtype", "fields": {"label": "sportsman", "title_en": "Sportsman", "title_ru": "\u0421\u043f\u043e\u0440\u0442\u0441\u043c\u0435\u043d", "title": "Sportsman"}}, {"pk": 2, "model": "sport.jobtype", "fields": {"label": "coach", "title_en": "Coach", "title_ru": "\u0422\u0440\u0435\u043d\u0435\u0440", "title": "Coach"}}, {"pk": 3, "model": "sport.jobtype", "fields": {"label": "other", "title_en": "other", "title_ru": "\u0418\u043d\u043e\u0435", "title": "other"}}, {"pk": 4, "model": "sport.jobtype", "fields": {"label": "business", "title_en": "business", "title_ru": "\u0421\u043f\u043e\u0440\u0442\u0438\u0432\u043d\u044b\u0439 \u0431\u0438\u0437\u043d\u0435\u0441", "title": "business"}}, {"pk": 5, "model": "sport.jobtype", "fields": {"label": "medicine", "title_en": "medicine", "title_ru": "\u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0430 \u0438 \u0444\u0438\u0437\u0438\u043e\u0442\u0435\u0440\u0430\u043f\u0438\u044f", "title": "medicine"}}, {"pk": 6, "model": "sport.jobtype", "fields": {"label": "jurisprudence", "title_en": "jurisprudence", "title_ru": "\u042e\u0440\u0438\u0441\u043f\u0440\u0443\u0434\u0435\u043d\u0446\u0438\u044f", "title": "jurisprudence"}}, {"pk": 7, "model": "sport.jobtype", "fields": {"label": "media", "title_en": "media", "title_ru": "\u041c\u0435\u0434\u0438\u0430 \u0438 PR", "title": "media"}}, {"pk": 8, "model": "sport.jobtype", "fields": {"label": "management", "title_en": "managment of club/sport organization", "title_ru": "\u041c\u0435\u043d\u0435\u0434\u0436\u043c\u0435\u043d\u0442 \u043a\u043b\u0443\u0431\u0430/\u0441\u043f\u043e\u0440\u0442\u0438\u0432\u043d\u043e\u0439 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438", "title": "managment of club/sport organization"}}, {"pk": 9, "model": "sport.jobtype", "fields": {"label": "agent", "title_en": "agent", "title_ru": "\u0410\u0433\u0435\u043d\u0442", "title": "agent"}}]

$ python3 tools/json2csv.py -i /tmp/JobType-2014-10-14.json -o /tmp/JobType-2014-10-14.csv 
[2014-10-14 09:48:58] INFO    => Read data from /tmp/JobType-2014-10-14.json...
[2014-10-14 09:48:58] INFO    => Found 9 items of "sport.jobtype" model
[2014-10-14 09:48:58] INFO    => Found id,title,title_ru,label,title_en fields for "sport.jobtype" model
[2014-10-14 09:48:58] INFO    => CSV data saved to "/tmp/JobType-2014-10-14.csv"

$ cat /tmp/JobType-2014-10-14.csv
id,title,title_ru,label,title_en
1,Sportsman,Спортсмен,sportsman,Sportsman
2,Coach,Тренер,coach,Coach
3,other,Иное,other,other
4,business,Спортивный бизнес,business,business
5,medicine,Медицина и физиотерапия,medicine,medicine
6,jurisprudence,Юриспруденция,jurisprudence,jurisprudence
7,media,Медиа и PR,media,media
8,managment of club/sport organization,Менеджмент клуба/спортивной организации,management,managment of club/sport organization
9,agent,Агент,agent,agent
</pre> 


2) Exclude some fields:

<pre>
$ python3 tools/json2csv.py -ex "title_ru,title_en" -i /tmp/JobType-2014-10-14.json -o /tmp/JobType-2014-10-14.csv 
[2014-10-14 09:49:44] INFO    => Read data from /tmp/JobType-2014-10-14.json...
[2014-10-14 09:49:44] INFO    => Found 9 items of "sport.jobtype" model
[2014-10-14 09:49:44] INFO    => Found id,title,label fields for "sport.jobtype" model
[2014-10-14 09:49:44] INFO    => CSV data saved to "/tmp/JobType-2014-10-14.csv"

$ cat /tmp/JobType-2014-10-14.csv 
id,title,label
1,Sportsman,sportsman
2,Coach,coach
3,other,other
4,business,business
5,medicine,medicine
6,jurisprudence,jurisprudence
7,media,media
8,managment of club/sport organization,management
9,agent,agent
</pre>
