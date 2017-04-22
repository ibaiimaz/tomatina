import moment from 'moment';

export default class UserStats {

  constructor(data) {
    this.name = data.name;
    this.status = data.status;
    this.start = moment(data.start);
    this.finish = this.start.add(25, 'm');
    this.pomodoros = data.pomodoros;
  }

  isFinished() {
    return this.start.isBefore(this.finish);
  }
}
