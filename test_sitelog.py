from sitelog import SiteLog
import sitelog.receiver as receiver

if __name__ == "__main__":
    # Læs fra en eksisterende sitelog
    sitelog = SiteLog('fyha_20161220.log')
    # ændr noget
    sitelog.header.code = 'FLAF'
    sitelog.write('test.log')

    # Lav en ny fra scratch
    log2 = SiteLog()
    log2.header.code = 'STAT'
    log2.form.prepared_by = 'Kristian Evers'
    log2.form.site_name = 'Station station'
    log2.form.site_code = 'STAT'
    log2.form.report_type = 'NEW'
    log2.form.date = '2020-02-05'

    log2.site_identification.date = '2020-02-05'
    log2.site_identification.bedrock_condition = 'FRESH'
    log2.gnss[0] = receiver.GnssReceiver()
    log2.gnss[1] = receiver.GnssReceiver()
    log2.gnss[0].receiver_type = 'Receiver 1'
    log2.gnss[1].receiver_type = 'Receiver 2'
    # Det ville gøre det lettere at bruge koden hvis man kunne gøre sådan her:
    #
    #  log2.gnss[0] = GnssReceiver(
    #      receiver_type = 'Receiver 1',
    #      sat_sys = 'GPS+GLONASS',
    #      firmware = '3.2.5',
    #      cutoff = '12',
    #      additional = 'Dette er en super sej receiver...'
    #  )
    log2.write('test2.log')


