import Vue from 'vue';

export default class PomodoroService {
  static createPomodoro() {
    return Vue.http.post('pomodoro', {});
  }
}
