from termgraph import termgraph as tg

class Letter:
    def __init__(self, _id, recipient, address, track, status, express):
        self._id = _id
        self.recipient = recipient
        self.recipient_short = '{0} {1}.{2}'.format(recipient['last'], recipient['first'][0], recipient['middle'][0])
        self.address = address
        self.address_short = '{0}, {1}, {2}, {3}'.format(address['country'], address['city'], address['street'], address['house_number'])
        self.track = track
        self.status = status
        self.express = express


    def get_data_from_table(self):
        return [self._id, self.recipient_short, self.address_short, self.track, self.status, self.express]

    def __str__(self):
        return "\n\tОтправитель: {0}\n\tАдрес: {1}\n\tОтслеживание: {2}\n\tЭкспресс: {3}\n".format(self.recipient_short, self.address_short, self.track, self.express)




def show_letter_plot(letters):
    labels = ['2007', '2008', '2009', '2010', '2011', '2012', '2014']
    data = [[183.32, 190.52], [231.23, 5.0], [16.43, 53.1], [50.21, 7.0], [508.97, 10.45], [212.05, 20.2], [30.0, 20.0]]
    normal_data = [[48.059508408796894, 50.0], [60.971862871927556, 0.0],
                   [3.080530401034929, 12.963561880120743],
                   [12.184670116429496, 0.5390254420008624],
                   [135.82632600258734, 1.4688443294523499],
                   [55.802608883139285, 4.096593359206555],
                   [6.737818025010781, 4.042690815006468]]
    len_categories = 2
    args = {'filename': 'data/ex4.dat', 'title': None, 'width': 50,
            'format': '{:<5.2f}', 'suffix': '', 'no_labels': False,
            'color': None, 'vertical': False, 'stacked': True,
            'different_scale': False, 'calendar': False,
            'start_dt': None, 'custom_tick': '', 'delim': '',
            'verbose': False, 'version': False}
    colors = [91, 94]
    print('Аналитика писем:')
    tg.stacked_graph(labels, data, normal_data, len_categories, args, colors)
    
