import moment from 'moment';

export default class UserStats {

  constructor(data) {
    this.name = data.username;
    this.status = data.status;
    this.start = data.started ? moment(data.started) : null;
    if (this.start) {
      this.finish = this.start.add(25, 'm');
    }
    this.pomodoros = data.pomodoros;

    if (!this.pomodoros) {
      this.isFirstPomodoro = true;
    }
  }

  isFinished() {
    return !this.isFirstPomodoro && this.start.isBefore(this.finish);
  }

  hasExpired() {
    return !this.isFirstPomodoro && this.finish && this.finish.isBefore(moment());
  }
}
