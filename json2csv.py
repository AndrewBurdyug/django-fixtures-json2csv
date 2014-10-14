import json
import argparse
import logging as log

parser = argparse.ArgumentParser(description='Convert django fixtures(JSON) ' +
                                 ' to CSV')
parser.add_argument('-i', '--input-file', type=open, required=True,
                    metavar='FILE', help='Logfile path')
parser.add_argument('-o', '--output-file', type=argparse.FileType('w'),
                    metavar='LOG LEVEL', default='INFO', required=True,
                    help='Log level, default: INFO')
parser.add_argument('-lf', '--log-file', type=argparse.FileType('w'),
                    metavar='FILE', help='Logfile path')
parser.add_argument('-lv', '--log-level', type=str, metavar='LOG LEVEL',
                    default='INFO', help='Log level, default: INFO')
parser.add_argument('-ex', '--exclude-fields', type=str,
                    metavar='EXCLUDE FIELDS',
                    help='Log level, format: "title,name,doc"')
args = parser.parse_args()


log_settings = dict(
    level=getattr(log, args.log_level),
    format='[%(asctime)s] %(levelname)-7s => %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

if args.log_file:
    log_settings['filename'] = args.log_file.name

log.basicConfig(**log_settings)


def detect_model(data):
    """Return Django model name.

    :param data: Dict of JSON items
    :returns: Django model name
    """
    return str(data[0]['model'])


def detect_fields(data):
    """Return JSON items fields.

    :param data: Dict of JSON items
    :returns: List of JSON items fields
    """
    fields = set([str(x) for x in data[0]['fields'].keys()])
    if args.exclude_fields:
        exclude_fields = set(
            [x.strip() for x in args.exclude_fields.split(',')])
        fields -= exclude_fields
    return fields


def parse_data(data, fields):
    """Yields items in CSV format.

    :param data: Dict of JSON items
    :yields: Str for CSV file
    """

    for item in data:
        row = "%s," % item['pk']
        row += ",".join([item['fields'][field_name] for field_name in fields])
        yield row

if __name__ == '__main__':
    data = json.load(args.input_file)
    fields = detect_fields(data)
    fields_plus = ['id']
    fields_plus.extend(fields)
    model_name = detect_model(data)

    log.debug(fields)
    log.debug(model_name)

    log.info('Read data from %s...', args.input_file.name)
    log.info('Found %d items of "%s" model', len(data), model_name)
    log.info('Found %s fields for "%s" model', ",".join(fields_plus),
             model_name)

    #  Write CSV header:
    args.output_file.write('%s\n' % ",".join(fields_plus))

    #  Write CSV data:
    for csv_line in parse_data(data, fields):
        args.output_file.write('%s\n' % csv_line)

    log.info('CSV data saved to "%s"', args.output_file.name)
