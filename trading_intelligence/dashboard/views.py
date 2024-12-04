from django.shortcuts import render
from journal.models import Journal
from django.contrib.auth.decorators import login_required
import json
from datetime import datetime


@login_required
def dashboard(request):

    user_journals = Journal.objects.filter(user=request.user)
    inicial_balance = 15000
    balance = inicial_balance + sum([journal.operation_balance for journal in user_journals])
    balance_net = balance - sum([journal.commission for journal in user_journals])
    profit_loss = sum([journal.operation_balance for journal in user_journals])
    n_operations = len(user_journals)
    lots = sum([journal.lots for journal in user_journals])
    # % win trades
    winning_trades = user_journals.filter(is_profit=True).count()
    win_rate = (winning_trades / n_operations if n_operations > 0 else 0) * 100  
    # % loss trades
    losing_trades = user_journals.filter(is_profit=False).count()
    loss_rate = (losing_trades / n_operations if n_operations > 0 else 0) * 100
    #best and worts trade
    best_trade = max([journal.operation_balance for journal in user_journals], default=0)
    worst_trade = min([journal.operation_balance for journal in user_journals], default=0)
    #gross profit and gross loss
    gross_profit = sum([journal.operation_balance for journal in user_journals if journal.operation_balance > 0])
    gross_loss = sum([journal.operation_balance for journal in user_journals if journal.operation_balance < 0])

  
    context = {
        'inicial_balance': inicial_balance,
        'balance': balance,
        'balance_net': balance_net,
        'profit_loss': profit_loss,
        'n_operations': n_operations,
        'lots': lots,
        'win_rate': win_rate,
        'loss_rate': loss_rate,
        'best_trade': best_trade,
        'worst_trade': worst_trade,
        'gross_profit': gross_profit,
        'gross_loss': gross_loss,
    }
    

    user_journals = Journal.objects.filter(user=request.user).order_by('open_datetime')
    
    # Initialize chart data
    chart_data = []
    running_balance = inicial_balance
    
    for journal in user_journals:
        running_balance += journal.operation_balance - journal.commission
        chart_data.append({
            'x': journal.open_datetime.strftime('%Y-%m-%d %H:%M:%S'),
            'y': round(running_balance, 2)
        })

    context.update({
        'chart_data': json.dumps(chart_data),
    })

    return render(request, 'tradingDash.html', context)
