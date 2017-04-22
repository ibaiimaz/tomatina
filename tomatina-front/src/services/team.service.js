import moment from 'moment';
import UserStats from '../models/userStats';
import Team from '../models/team';

export default class TeamService {

  static getUserTeams(/*userId*/) {
    const teams = [
      new Team({ name: 'team 1' }),
      new Team({ name: 'team 2' }),
      new Team({ name: 'team 3' }),
    ];
    return Promise.resolve(teams);
  }

  static getTeamStats() {
    const result = [
      new UserStats({
        name: 'alfredo',
        status: 'working',
        start: moment().subtract(20, 'm'),
        pomodoros: [
          { start: moment().subtract(20, 'm') },
          { start: moment().subtract(50, 'm') },
          { start: moment().subtract(200, 'm') },
        ],
      }),

      new UserStats({
        name: 'ibai',
        status: 'working',
        start: moment().subtract(120, 'm'),
        pomodoros: [
          { start: moment().subtract(120, 'm') },
          { start: moment().subtract(150, 'm') },
          { start: moment().subtract(220, 'm') },
          { start: moment().subtract(300, 'm') },
        ],
      }),
      new UserStats({
        name: 'fernando',
        status: 'resting',
        start: moment().subtract(80, 'm'),
        pomodoros: [
          { start: moment().subtract(80, 'm') },
          { start: moment().subtract(200, 'm') },
        ],
      }),
    ];
    return Promise.resolve(result);
  }
}
