
section_table = {
                "index":    {   "index": True   },
                "specific": {   "index": False, "title": True, "specific": True,
                                "legacy_intro": False, "new_intro": True,  "form_intro": False,
                                "holder": True, "holder_contact": True, "ietf_contact": True,
                                "ietf_doc": True, "patent_info": True, "licensing": True,
                                "submitter": True, "notes": True, "form_submit": False,
                                "disclosure_type": "Specific", "form_legend": False, 
                                "per_rfc_disclosure": True, "also_specific": False,
                            },
                "generic": {   "index": False, "title": True, "generic": True,
                                "legacy_intro": False, "new_intro": True,  "form_intro": False,
                                "holder": True, "holder_contact": True, "ietf_contact": False,
                                "ietf_doc": False, "patent_info": True, "licensing": True,
                                "submitter": True, "notes": True, "form_submit": False,
                                "disclosure_type": "Generic", "form_legend": False, 
                                "per_rfc_disclosure": False, "also_specific": True,
                            },
                "third-party": {"index": False, "title": True, "third_party": True, 
                                "legacy_intro": False, "new_intro": True,  "form_intro": False,
                                "holder": True, "holder_contact": False, "ietf_contact": True,
                                "ietf_doc": True, "patent_info": True, "licensing": False,
                                "submitter": False, "notes": False, "form_submit": False,
                                "disclosure_type": "Third Party", "form_legend": False, 
                                "per_rfc_disclosure": False, "also_specific": False,
                            },
                "legacy":   {   "index": False, "title": True, "legacy": True,
                                "legacy_intro": True, "new_intro": False,  "form_intro": False,
                                "holder": True, "holder_contact": True, "ietf_contact": False,
                                "ietf_doc": True, "patent_info": False, "licensing": False,
                                "submitter": False, "notes": False, "form_submit": False,
                                "disclosure_type": "Legacy", "form_legend": False, 
                                "per_rfc_disclosure": False, "also_specific": False,
                            },
            }
