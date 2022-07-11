from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color


class WidgetsExample(GridLayout):
  my_text = StringProperty("0")
  count = 0
  state = BooleanProperty(False)
  # slider_txt = StringProperty("--")
  text_input_str = StringProperty("foo")

  def on_button_click(self):
    if self.state:
      print("Button Enabled")
      self.count += 1
      self.s = ("", "s")[self.count > 1]
      self.my_text = f"{self.count}\ntime{self.s}"
    else:
      print("Button Disabled")

  def on_toggle_button_state(self, widget):
    ws = ("ON", "OFF")[widget.state=="normal"]
    self.state = (True, False)[widget.state=="normal"]
    widget.text = ws
    print(f"toggle state: {widget.state} = {ws}")

  def on_switch_active(self, widget):
    sa = ("ON", "OFF")[widget.active==False]
    print(f"Switch: {widget.active} = {sa}")

  # def on_slider_value(self, widget):
  #   # self.slider_txt = f"{int(widget.value)}"
  #   print(f"Slider: {int(widget.value)}")

  def validation(self, widget):
    self.text_input_str = widget.text
    
class StackLayoutExample(StackLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    for i in range(0, 100):
      # self.orientation = 'lr-bt'
      b = Button(
      text=str(i+1),
      size_hint=(None, None),
      size=(dp(100), dp(100))
      )
      self.add_widget(b)

# class GridLayoutExample(GridLayout):
#   pass

class AnchorLayoutExample(AnchorLayout):
  pass

class BoxLayoutExample(BoxLayout):
  pass
  # def __init__(self, **kwargs):
  #   super().__init__(**kwargs)

  #   b1 = Button(text="A")
  #   b2 = Button(text="B")
  #   b3 = Button(text="C")
    
  #   self.add_widget(b1)
  #   self.add_widget(b2)
  #   self.add_widget(b3)

class MainWidget(Widget):
  pass

class TheLabApp(App):
  pass

class CanvasExample1(Widget):
  pass

class CanvasExample2(Widget):
  pass

class CanvasExample3(Widget):
  pass

class CanvasExample4(Widget):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    with self.canvas:
      Line(points=(100, 100, 400, 400), width=2)
      Color(0, 1, 0)
      Line(circle=(400, 200, 80), width=2)
      Line(rectangle=(700, 500, 150, 100), width=5)
      self.rect = Rectangle(pos=(700, 200), size=(150, 200))

  def on_click(self):
    x, y = self.rect.pos
    w, h = self.rect.size
    inc = dp(10)
    diff = self.width - (x+w)

    print(f"width: {self.width}")
    print(f"r pos: {self.rect.pos}")
    print(f"x+150: {x+150}\n")

    if diff < inc:
      inc = diff
      
    x += inc
    self.rect.pos = (x, y)

class CanvasExample5(Widget):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.ball_size = dp(50)
    self.vx = dp(3)
    self.vy = dp(4)
    with self.canvas:
      self.ball = Ellipse(pos=(100, 100), size=(self.ball_size, self.ball_size))
    Clock.schedule_interval(self.update, 1/60)
    
  def on_size(self, *args):
    # print(f"on_size:\nw: {self.width}\nh: {self.height}")
    self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)
  
  def update(self, dt):
    x, y = self.ball.pos
    x += self.vx
    y += self.vy
    
    if y + self.ball_size > self.height:
      y = self.height - self.ball_size
      self.vy = -self.vy

    if x + self.ball_size > self.width:
      x = self.width - self.ball_size
      self.vx = -self.vx

    if y < 0:
      y = 0
      self.vy = -self.vy

    if x < 0:
      x = 0
      self.vx = -self.vx
      
    self.ball.pos = (x, y)

class CanvasExample6(Widget):
  pass

class CanvasExample7(BoxLayout):
  pass

if __name__ == "__main__":
  TheLabApp().run()
