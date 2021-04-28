# coding: utf-8

import crawlExcel
import misc
import processExcel
import genIcs


form_url, form_inputs = crawlExcel.get_text()
crawlExcel.login(form_url, form_inputs)
uid = crawlExcel.getUID()
crawlExcel.writeExcel(uid)

cal_raw_data = processExcel.process()

genIcs.gen(cal_raw_data)
