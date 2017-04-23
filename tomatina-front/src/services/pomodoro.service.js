import Vue from 'vue';

export default class PomodoroService {
  static createPomodoro(userId) {
    return Vue.http.post('pomodoro/', { user_id: userId });
  }
}
