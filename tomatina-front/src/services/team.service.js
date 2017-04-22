import UserStats from '../models/userStats';

export default class TeamService {
  static getTeamStats() {
    const result = [
      new UserStats({
        name: 'alfredo',
        status: 'working',
        start: new Date(),
        pomodoros: [{
          start: new Date(),
        }],
      }),

      new UserStats('alfredo'),
      new UserStats('ibai'),
      new UserStats('fernando'),
    ];
    return Promise.resolve(result);
  }
}
