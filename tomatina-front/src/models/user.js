export default class User {
  constructor(data) {
    this.id = data.id;
    this.name = data.username;
    this.teams = data.groups;
  }
}
