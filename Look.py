app.layout = html.Div(
	children=[
		html.H1(children="1 Analytics",),
		html.P(
			children="Analyze the behavior of x"
			" and the number of x currently"
			" between y and z".
			),
			dcc.Graph(
				figure={
					"data": [
					{
							"x": data["Date"],
							"y": data["AveragePrice"],
							"type": "lines",
					},
				],
				"layout": {"title": "AveragePrice of Avocados"},
