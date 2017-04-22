import User from '../models/user';

export default class TeamService {
  static getTeam() {
    const result = [
      new User('alfredo'),
      new User('ibai'),
      new User('fernando'),
    ];
    return Promise.resolve(result);
  }
}
