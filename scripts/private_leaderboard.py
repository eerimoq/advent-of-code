import json
import argparse
from datetime import datetime


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('database')
    parser.add_argument('day')
    args = parser.parse_args()

    with open(args.database, 'r') as fin:
        private_leaderboard = json.load(fin)

    members = []

    for member in private_leaderboard['members'].values():
        star_1_ts = 999999999999999999
        star_2_ts = 999999999999999999
        completion_day = member['completion_day_level'].get(args.day)

        if completion_day is not None:
            star_1_ts = int(completion_day['1']['get_star_ts'])
            star_2 = completion_day.get('2')

            if star_2 is not None:
                star_2_ts = int(star_2['get_star_ts'])

        members.append((member['name'],
                        max(star_1_ts, star_2_ts),
                        star_1_ts,
                        star_2_ts))

    day_start_ts = int(datetime.fromisoformat(
        f'2021-12-{int(args.day):02} 06:00:00+01:00').timestamp())
    print('NAME                                     STAR 1  STAR 2')

    for member in sorted(members, key=lambda v: v[1]):
        star_1_time = member[2] - day_start_ts
        star_2_time = member[3] - day_start_ts
        print(f'{str(member[0]):40} {star_1_time:6} {star_2_time:7}')


if __name__ == '__main__':
    main()
