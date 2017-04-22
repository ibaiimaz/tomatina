import Vue from 'vue';
import User from '../models/user';

export default class UserService {

  static getUser(username) {
    const promise = Vue.http.get('users', {})
      .then((response) => {
        const users = response.body;
        const filtered = users.filter(user => user.username === username);
        return filtered.length ? new User(filtered[0]) : null;
      }, (error, a, b, c) => {
        throw error;
      });
    return promise;
  }
}
