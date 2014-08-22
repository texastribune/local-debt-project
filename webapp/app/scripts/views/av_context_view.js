app.Views.AVContext = Marionette.CompositeView.extend({
  template: JST['app/scripts/templates/av_context.html'],
  childView: app.Views.AVContextRow,
  childViewContainer: 'tbody',
});
