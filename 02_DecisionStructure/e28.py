tipo_carne = input('Digite o tipo da carne\n\nFD-File Duplo\nA-Alcatra\nP-Picanha: ')
qtde_carne = int(input('Digite a qtde de carne em kg: '))
tipo_pgmto = input('Digite o tipo de pagamento (C-Cartao ou D-Dinheiro): ')

if tipo_pgmto == 'C':

    if tipo_carne == 'FD':
        if qtde_carne > 5:
            val_fd = qtde_carne * 5.8
        else:
            val_fd = qtde_carne * 4.9
        tot_des = val_fd - (val_fd * 0.05)
        print('\nCarne tipo: FD - File Duplo\nQtde da carne em kg: {}\nPreco Total: {}\nPagamento no Cartao\nValor do desconto: {}\nValor a pagar: {:.2f}'.format(qtde_carne, val_fd, (val_fd * 0.05), tot_des ))

    elif tipo_carne == 'A':
        if qtde_carne > 5:
            val_fd = qtde_carne * 6.8
        else:
            val_fd = qtde_carne * 5.9
        tot_des = val_fd - (val_fd * 0.05)
        print('\nCarne tipo: A - Alcatra\nQtde da carne em kg: {}\nPreco Total: {}\nPagamento no Cartao\nValor do desconto: {}\nValor a pagar: {:.2f}'.format(qtde_carne, val_fd, (val_fd * 0.05), tot_des ))

    elif tipo_carne == 'P':
        if qtde_carne > 5:
            val_fd = qtde_carne * 7.8
        else:
            val_fd = qtde_carne * 6.9
        tot_des = val_fd - (val_fd * 0.05)
        print('\nCarne tipo: P - Picanha\nQtde da carne em kg: {}\nPreco Total: {}\nPagamento no Cartao\nValor do desconto: {}\nValor a pagar: {:.2f}'.format(qtde_carne, val_fd, (val_fd * 0.05), tot_des ))

    else:
        print('Esse tipo de carne nao esta no cadastro')

elif tipo_pgmto == 'D':

        if tipo_carne == 'FD':
            if qtde_carne > 5:
                val_fd = qtde_carne * 5.8
            else:
                val_fd = qtde_carne * 4.9
            print('\nCarne tipo: FD - File Duplo\nQtde da carne em kg: {}\nPreco Total: {}\nPagamento no Dinheiro\nValor do desconto: {}\nValor a pagar: {:.2f}'.format(qtde_carne, val_fd, 0, val_fd ))

        elif tipo_carne == 'A':
            if qtde_carne > 5:
                val_fd = qtde_carne * 6.8
            else:
                val_fd = qtde_carne * 5.9
            print('\nCarne tipo: A - Alcatra\nQtde da carne em kg: {}\nPreco Total: {}\nPagamento no Dinheiro\nValor do desconto: {}\nValor a pagar: {:.2f}'.format(qtde_carne, val_fd, 0, val_fd ))

        elif tipo_carne == 'P':
            if qtde_carne > 5:
                val_fd = qtde_carne * 7.8
            else:
                val_fd = qtde_carne * 6.9
            print('\nCarne tipo: P - Picanha\nQtde da carne em kg: {}\nPreco Total: {}\nPagamento no Dinheiro\nValor do desconto: {}\nValor a pagar: {:.2f}'.format(qtde_carne, val_fd, 0, val_fd ))

        else:
            print('Esse tipo de carne nao esta no cadastro')

else:
    print('A forma de pagamento nao eh valida!')
