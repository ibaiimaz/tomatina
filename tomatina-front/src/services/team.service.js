import moment from 'moment';
import Vue from 'vue';

import Team from '../models/team';

export default class TeamService {

  static getUserTeams(/*userId*/) {
    return Vue.http.get('groups/')
      .then(
        (response) => response.body.map((team) => new Team(team))
      );
  }
}
