# List Of Things To Do

* Build An Excellent User Interface

    * CSS Framework - Clear and Focused

    * switch color to something lighter when they get results


* Big Parser

    * Collect Reliable Resources

    * Artificial Intelligence

    * Generate data

        * URL generation - DONE

            * python script: takes a domain and outputs all urls under it

            * populates a csv file with the urls -> urls go under "url" column

        * keyword generation

            1. takes url

            2. generates the html data for that url

            3. passes the html data to a parser which strips all html tags

            4. takes the pure page content and passes it to a filler word stripper to output only a list of key words

            5. takes list of key words and generate a new list of related words *plus* the original key words

            6. fills the respective csv URL row with the keywords under column "Key words"
