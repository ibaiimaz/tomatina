import moment from 'moment';
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
}
