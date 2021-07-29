"""Sample sailor program."""
from sailor import sailor as s


def do_exit(app):
    app.exit = True


options = [
    'option 1',
    'option 2',
    s.Option('option 3', 'three is special'),
    'option 4',
    'option 5',
]


def show_popup(app):
    popup = s.Popup(s.Stacked([
        s.Text('Just a popup to show you something')
    ]), on_close=lambda x, y: None)
    popup.show(app)


def show_changed(app, was, tobe):
    popup = s.Popup(s.Stacked([
        s.Text(f'Value from [{was}] to [{tobe}]!')
    ]), on_close=lambda x, y: None)
    popup.show(app)


def complete_fn(word):
    candidates = ['foo', 'bar', 'baz', 'sailor', 'curses', 'walk', 'hello', 'world']
    return [w for w in candidates if w.startswith(word)]


def main():
    SWITCHES = [
        s.Text('Switchable 1'),
        s.Button("Switchable 2"),
        s.Panel([s.Text('Bigger than you thought')], caption=s.Text('Switchable 3'))
    ]
    current_switchable = [0]  # Reference hack
    switchable = s.SwitchableControl(SWITCHES[current_switchable[0]])

    def do_next(app):
        current_switchable[0] = (current_switchable[0] + 1) % len(SWITCHES)
        switchable.switch(SWITCHES[current_switchable[0]], app)

    root = s.Panel(
        caption=s.Text('Control showcase'),
        controls=[
            s.Labeled('Text', s.Composite([
                s.Text('This is plain text'),
                s.Text('in a different color', fg=s.red),
            ], margin=1)),
            s.Labeled('Panel', s.Panel([s.Text('Inner panel just because we can')])),
            s.Labeled('SelectList', s.SelectList(options, 0)),
            s.Labeled('Combo', s.Combo(options, on_changed=show_changed)),
            s.Labeled('DateCombo', s.DateCombo()),
            s.Labeled('Time', s.Time()),
            s.Labeled('Popup', s.Button('Hit me', on_click=show_popup)),
            s.Labeled('Edit', s.Edit('you can edit this')),
            s.Labeled('AutoComplete', s.AutoCompleteEdit('type here', [
                'history1',
                'history2'
            ], complete_fn)),
            s.Labeled('SwitchableCtrl', switchable),
            s.Labeled('', s.Button('Next', on_click=do_next)),
            s.Labeled('Button', s.Button('Exit', on_click=do_exit)),
        ])

    s.walk(root)


if __name__ == '__main__':
    main()
