import os
import sys
import django
from pathlib import Path

# Ensure DJANGO_SETTINGS_MODULE is set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loja.settings')
django.setup()

from django.core.management import call_command
from django.contrib.auth.models import User
from produto.models import Produto, Variacao

def main():
    db_url = os.environ.get('DATABASE_URL') or os.environ.get('POSTGRES_URL')
    if not db_url:
        print("❌ Error: DATABASE_URL environment variable is not set!")
        print("Usage:")
        print("  DATABASE_URL='postgresql://postgres:POCOYO2007%24!@db.htarcxxkjpfuejdqqrjq.supabase.co:5432/postgres' python seed_supabase.py")
        sys.exit(1)

    print("🚀 1. Running Django migrations on Supabase Database...")
    call_command('migrate')
    print("✅ Migrations completed successfully!")

    print("\n👤 2. Creating Superuser 'admin'...")
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("✅ Superuser 'admin' created with password 'admin123'!")
    else:
        print("ℹ️ Superuser 'admin' already exists.")

    print("\n🌸 3. Seeding Floriculture Sample Products...")
    
    # 1. Buquê de Rosas
    p1, _ = Produto.objects.get_or_create(
        nome='Buquê Premium 12 Rosas Vermelhas',
        defaults={
            'descricao_curta': 'A clássica declaração de amor com rosas vermelhas selecionadas e embalagem artesanal.',
            'descricao_longa': 'Nosso Buquê Premium é confeccionado à mão por mestres floristas com 12 rosas vermelhas de haste longa importadas, folhagens nobres de eucalipto e acabamento elegante em papel kraft ecológico e fita de cetim.',
            'imagem': 'produto_imagens/2026/09/buque_rosas.jpg',
            'preco_marketing': 189.90,
            'preco_marketing_promocional': 159.90,
            'tipo': 'V'
        }
    )
    if not p1.variacao_set.exists():
        Variacao.objects.create(produto=p1, nome='Tamanho Padrão (12 Rosas)', preco=189.90, preco_promocional=159.90, estoque=25)
        Variacao.objects.create(produto=p1, nome='Tamanho Luxo (24 Rosas + Vaso)', preco=299.90, preco_promocional=259.90, estoque=15)
        Variacao.objects.create(produto=p1, nome='Com Caixa de Bombons Gourmet', preco=229.90, preco_promocional=199.90, estoque=20)

    # 2. Orquídea
    p2, _ = Produto.objects.get_or_create(
        nome='Orquídea Phalaenopsis Branca Dupla',
        defaults={
            'descricao_curta': 'Elegante orquídea de duas hastes em vaso cerâmico trabalhado.',
            'descricao_longa': 'A Orquídea Phalaenopsis Branca simboliza pureza, sofisticação e harmonia. Ideal para decoração de interiores, escritórios e presentes refinados.',
            'imagem': 'produto_imagens/2026/09/orquidea_branca.jpg',
            'preco_marketing': 149.00,
            'preco_marketing_promocional': 129.90,
            'tipo': 'V'
        }
    )
    if not p2.variacao_set.exists():
        Variacao.objects.create(produto=p2, nome='Cachepô Cerâmica Branca', preco=149.00, preco_promocional=129.90, estoque=18)
        Variacao.objects.create(produto=p2, nome='Vaso de Vidro Transparente', preco=169.00, preco_promocional=149.90, estoque=12)

    # 3. Girassóis
    p3, _ = Produto.objects.get_or_create(
        nome='Arranjo Flores do Campo & Girassóis',
        defaults={
            'descricao_curta': 'Um raio de sol em forma de flores! Girassóis radiantes combinados com margaridas.',
            'descricao_longa': 'Traga a alegria e a energia do campo para quem você ama. Este arranjo vibrante combina girassóis recém-colhidos, gipsófilas e folhagens tropicais.',
            'imagem': 'produto_imagens/2026/09/girassois.jpg',
            'preco_marketing': 139.90,
            'preco_marketing_promocional': 119.90,
            'tipo': 'V'
        }
    )
    if not p3.variacao_set.exists():
        Variacao.objects.create(produto=p3, nome='Tamanho Médio', preco=139.90, preco_promocional=119.90, estoque=30)
        Variacao.objects.create(produto=p3, nome='Tamanho Grande', preco=189.90, preco_promocional=169.90, estoque=15)

    # 4. Cesta de Flores & Café
    p4, _ = Produto.objects.get_or_create(
        nome='Cesta Especial Flores & Café da Manhã',
        defaults={
            'descricao_curta': 'Cesta artesanal com arranjo de flores frescas e itens selecionados de café.',
            'descricao_longa': 'Uma experiência completa para surpreender logo no início do dia! Inclui arranjo de flores da estação, pães artesanais, geleia e café gourmet.',
            'imagem': 'produto_imagens/2026/09/cesta_flores.jpg',
            'preco_marketing': 249.90,
            'preco_marketing_promocional': 219.90,
            'tipo': 'V'
        }
    )
    if not p4.variacao_set.exists():
        Variacao.objects.create(produto=p4, nome='Cesta Individual', preco=249.90, preco_promocional=219.90, estoque=10)
        Variacao.objects.create(produto=p4, nome='Cesta Casal (Dupla)', preco=329.90, preco_promocional=289.90, estoque=8)

    # 5. Suculenta
    p5, _ = Produto.objects.get_or_create(
        nome='Jardim de Suculentas em Cachepô Terracota',
        defaults={
            'descricao_curta': 'Composição exclusiva de suculentas e cactos em vaso decorativo.',
            'descricao_longa': 'Ideal para quem busca plantas de fácil manutenção e alta durabilidade. Uma linda combinação de variedades de suculentas dispostas sobre substrato especial.',
            'imagem': 'produto_imagens/2026/09/suculenta.jpg',
            'preco_marketing': 89.90,
            'preco_marketing_promocional': 69.90,
            'tipo': 'V'
        }
    )
    if not p5.variacao_set.exists():
        Variacao.objects.create(produto=p5, nome='Cachepô Terracota', preco=89.90, preco_promocional=69.90, estoque=40)
        Variacao.objects.create(produto=p5, nome='Cachepô Mármore', preco=109.90, preco_promocional=89.90, estoque=20)

    # 6. Lírios
    p6, _ = Produto.objects.get_or_create(
        nome='Lírios Brancos & Gipsófilas em Vaso',
        defaults={
            'descricao_curta': 'Lírios brancos perfumados com delicados ramos de gipsófilas em vaso de cristal.',
            'descricao_longa': 'Um arranjo clássico que transmite nobreza, paz e elegância. Os lírios brancos possuem um perfume suave e marcante.',
            'imagem': 'produto_imagens/2026/09/lirios.jpg',
            'preco_marketing': 179.90,
            'preco_marketing_promocional': 149.90,
            'tipo': 'V'
        }
    )
    if not p6.variacao_set.exists():
        Variacao.objects.create(produto=p6, nome='Arranjo Médio (3 Hastes)', preco=179.90, preco_promocional=149.90, estoque=15)
        Variacao.objects.create(produto=p6, nome='Arranjo Luxo (5 Hastes)', preco=239.90, preco_promocional=199.90, estoque=10)

    print("✅ Sample products and variations seeded successfully in Supabase!")
    print("\n🎉 Your Supabase Database is 100% ready for Vercel!")

if __name__ == '__main__':
    main()
