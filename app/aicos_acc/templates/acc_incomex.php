{% extends "acct_base.html" %}
{% block body %}
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-8">
                        <div class="card">
                            <div class="card-header bg-light">
                                <h3>New Income</h3>
                            </div>
                            <div class="card-body">
                                <div class="row mt-4">
                                    <div class="col-md-6">
                                        <div class="form-group">
                                            <label for="single-select">Income Type</label>
                                            <select id="single-select" class="form-control">
                                                <option>Choose income source</option>
                                                <option>Umusanzu</option>
                                                <option>Umugabane</option>
                                                <option>Amande</option>
                                            </select>
                                        </div>
                                        <div class="form-group">
                                            <label for="placeholder-input" class="form-control-label">Amount</label>
                                            <input id="placeholder-input" class="form-control" placeholder="Enter income amount">
                                        </div>
                                        <!--
                                        <div class="form-group">
                                            <label for="single-select">Channel</label>
                                            <select id="single-select" class="form-control">
                                                <option>Income Channel</option>
                                                <option>Bank Deposit</option>
                                                <option>Cash</option>
                                            </select>
                                        </div>
                                        <div class="form-group">
                                            <label for="single-select">Choose Bank Account</label>
                                            <select id="single-select" class="form-control">
                                                <option>Bank Account</option>
                                                <option>AB Bank (10122587)</option>
                                                <option>BK (7874580012)</option>
                                                <option>BPR (774400212)</option>
                                            </select>
                                        </div>
                                        <div class="form-group">
                                            <label for="single-select">Bank Operation Type</label>
                                            <select id="single-select" class="form-control">
                                                <option>Choose Bank Operation</option>
                                                <option>Deposti</option>
                                                <option>Transfer</option>
                                                <option>Check</option>
                                            </select>
                                        </div>
                                        -->
                                        <div class="form-group">
                                            <label for="placeholder-input" class="form-control-label">Date</label>
                                            <input type="date" id="placeholder-input" class="form-control" placeholder="Date">
                                        </div>
                                         <div class="btn btn-outline-primary"> Save Income </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
{% endblock %}