for DIR_NAME in `find download_PFDs/pdf_documents/ -mindepth 1 -type d`; do utils/count_pages_per_doc.sh $DIR_NAME >> PFD_doc_stats.csv; done;
echo -e "filename\tnum_pages" > PFD_doc_stats.csv 
