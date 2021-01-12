from fpdf import FPDF
import comparison_data

WIDTH = 210
HEIGHT = 297

def create_report(filename='report.pdf'):
    # create pdf and add page
    pdf = FPDF()
    pdf.add_page()
    
    # set up title
    pdf.set_font('Arial', '', 22)  
    pdf.ln(5)
    pdf.write(5, "U.S. Bike Share System Comparison: 2017-2019")
    pdf.ln(8)
    pdf.set_font('Arial', '', 14)
    pdf.write(5, 'By: Martin Pleynet')

    # Section 1: Introduction
    pdf.ln(10)
    pdf.set_font('Arial', '', 18)
    pdf.write(10, 'Introduction')
    pdf.ln(10)
    pdf.set_font('Arial', '', 14)
    pdf.write(5, "In this report, I aim to compare nine different bike share systems across the U.S. using rider data from each city spanning from 2017 to 2019. Those cities are Boston, Chicago, DC, LA, Minneapolis, New York, Philadelphia, Pittsburgh, and Portland.")
    pdf.ln(10)
    pdf.write(5, "I've developed five different metrics to compare these systems:")
    pdf.ln(6)
    pdf.set_x(20)
    pdf.write(5, '1. Bikes per Thousand People')
    pdf.ln(6)
    pdf.set_x(20)
    pdf.write(5, '2. Trips per Bicycle per day')
    pdf.ln(6)
    pdf.set_x(20)
    pdf.write(5, '3. Stations per Square Mile')
    pdf.ln(6)
    pdf.set_x(20)
    pdf.write(5, '4. Subscribership Percentage')
    pdf.ln(6)
    pdf.set_x(20)
    pdf.write(5, '5. Customer/Subscriber Trip Duration')
    pdf.ln(6)
    pdf.write(5, "The results of each of these metrics have been plotted by city below.")

    # Section 2: Bikes per thousand people - BPT
    pdf.ln(10)
    pdf.set_font('Arial', '', 18)
    pdf.write(10, "Bikes per Thousand People (BPT)")
    pdf.ln(10)
    pdf.set_font('Arial', '', 14)
    pdf.write(5, "To calculate BPT, I first found the number of bikes for each year using the rider data, and then, collected each city's population from their respective Wikipedia pages. I proceeded to divide the number of bikes times 1000 by the city population. The calculated BPT values produced the following graph.")
    
    comparison_data.bpt_graph('bpt.png')
    pdf.image('bpt.png', WIDTH/2-WIDTH/4, 145, WIDTH/2)
    pdf.set_y(226)
    pdf.write(5, "During this three-year span, all cities saw an overall increase in BPT with the exception of Chicago. Boston and DC saw the greatest increase in BPT from 2.62 to 6.71 and 6.69 to 8.58 respectively. These increases suggest that more bikes were added to each city's system to reflect the increased bike share usage.")

    # Section 3: trips per bicycle per day
    pdf.ln(10)
    pdf.set_font('Arial', '', 18)
    pdf.write(10, "Trips per Bicycle per Day (TPB)")
    pdf.ln(10)
    pdf.set_font('Arial', '', 14)
    pdf.write(5, "To calculate TPB, I first found the total number of trips for each year using the rider data, and then, divided by the number of bikes in the system found above. The calculated TPB values produced the following graph.")

    pdf.add_page()
    comparison_data.tpb_graph('tpb.png')
    pdf.image('tpb.png', WIDTH/2-WIDTH/4, 10, WIDTH/2)
    pdf.set_y(95)
    pdf.write(5, "Cities like Boston and DC have seen a reduction in TPB from 1.99 to 1.48 and 2.21 to 1.53 respectively, which results directly from an increase in the total number of bikes in their respective systems seen in the previous section. However, cities like LA, Pittsburgh, and Portland all have low TPB's which coupled with their low BPT's suggests that their systems are under used compared to their counterparts. Finally, given New York's high TPB and low BPT, their system may benefit from an influx of bikes to reduce the wear on individual bikes.")

    # Section 4: Stations per square mile - SPS
    pdf.ln(10)
    pdf.set_font('Arial', '', 18)
    pdf.write(10, "Stations per Square Mile (SPS)")
    pdf.ln(10)
    pdf.set_font('Arial', '', 14)
    pdf.write(5, "To calculate SPS, I first found the number of stations for each year using the rider data, and then, collected each city's land size in square miles from their respective Wikipedia pages. I proceeded to divide the number of stations by the city square mileage. The calculated SPS values produced the following graph.")

    comparison_data.sps_graph('sps.png')
    pdf.image('sps.png', WIDTH/2-WIDTH/4, 168, WIDTH/2)
    pdf.set_y(250)
    pdf.write(5, "Pittsburgh leads all systems with the highest SPS with nearly 16, with the jump from 2017 to 2018 being quite perplexing as it does not much the relative increase in BPT. DC and Boston come next with an SPS of 10.66 and 7.37 respectively. Their increases in SPS seem to proportionately match their increases in BPT which makes sense as an increase in bikes requires an increase in stations for those bikes.")                                        

    # Section 5: Subscribership percentage
    pdf.add_page()
    pdf.ln(5)
    pdf.set_font('Arial', '', 18)
    pdf.write(10, "Subscribership Percentage (SP)")
    pdf.ln(10)
    pdf.set_font('Arial', '', 14)
    pdf.write(5, "Each bike share system allows people to purchase subscriptions or be one time customers. As a result, all trips are broken down into either subscriber or customer trips. I am using the percentage of subscriber trips in a year as a proxy for subscribership percentage. To calculate SP, I first found the total number of subscriber trips for each year, and then, I found the total number of trips for each year using the rider data. I proceeded to divide the number of subscriber trips by the total number of trips and multiplied by 100. The calculated SP values produced the graph below.")

    comparison_data.sub_graph('sub.png')
    pdf.image('sub.png', WIDTH/2-WIDTH/4, 65, WIDTH/2)
    pdf.set_y(150)
    pdf.write(5, "New York leads all bike share systems with the highest subscribership percentage at 89% with Boston, Chicago, and DC close behind. It seems that the more established bike share systems, being the four previously listed, have the highest subscribership percentages, while smaller and newer systems such as Portland and Pittsburgh have subscribership percenatges about half that of New York's.")

    # Section 6: Customer/Subscriber Median Ride Duration
    pdf.ln(10)
    pdf.set_font('Arial', '', 18)
    pdf.write(10, "Customer/Subscriber Trip Duration")
    pdf.ln(10)
    pdf.set_font('Arial', '', 14)
    pdf.write(5, 'To calculate the trip duration for both groups of riders, I took the median trip duration in minutes of all trips over the three-year period for customers and subscribers. The resulting trip duration medians for each city produced the graph below.')

    comparison_data.td_graph('td.png')
    pdf.image('td.png', WIDTH/2-WIDTH/4, 208, WIDTH/2)
    
    pdf.add_page()
    pdf.ln(5)
    pdf.write(5, 'The specific bike share system appears to have no effect on subscriber and customer habits. For each city, the median subscriber trip duration was around 10 mintues, while the median customer trip duration was around 20 minutes, double that of subscribers. This is to be expected since based on the payment structure, subscribers get untlimited trips in a month while customers must pay for each trip they take. As a result, customers are more inclined to take advantage of each trip and ride for longer.')

    # Section 7: Conclusion
    pdf.ln(10)
    pdf.set_font('Arial', '', 18)
    pdf.write(10, "Conclusion")
    pdf.ln(10)
    pdf.set_font('Arial', '', 14)
    pdf.write(5, 'In conclusion, the bike share systems of Boston and DC seem to be the most established, utilized, and best updated of the nine systems, with New York close behind. For many of these metrics, there is a noticable change present in their graphs over the three-year period suggesting that these systems are being altered and catered to best fit the usage they face. The combination of a high BPT and SPS, a medium TPB, and a high subscribership percentage places these two bike share systems a pedal stroke ahead of the rest.')

    pdf.output(filename)

if __name__ == '__main__':
    create_report('final_report.pdf')

    
    
    
    


