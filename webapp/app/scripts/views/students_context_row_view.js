app.Views.StudentsContextRow = Marionette.ItemView.extend({
  template: JST['app/scripts/templates/students_context_row.html'],
  tagName: 'tr'
});

_.extend(app.Views.StudentsContextRow.prototype, app.Mixins.Helpers);
