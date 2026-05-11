const API_URL = "http://127.0.0.1:8000/api/v1/products/paginated";

const productsContainer = document.getElementById("productsContainer");
const pageInfo = document.getElementById("pageInfo");

const prevPageButton = document.getElementById("prevPage");
const nextPageButton = document.getElementById("nextPage");

const SEARCH_URL = "http://127.0.0.1:8000/api/v1/products";
const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");

const PRODUCT_URL = "http://127.0.0.1:8000/api/v1/products/";

const productForm = document.getElementById("productForm");

const nomeInput = document.getElementById("nome");
const skuInput = document.getElementById("sku");
const codigoBarrasInput = document.getElementById("codigo_barras");
const precoCustoInput = document.getElementById("preco_custo");
const precoVendaInput = document.getElementById("preco_venda");
const quantidadeInput = document.getElementById("quantidade");
const estoqueMinimoInput = document.getElementById("estoque_minimo");
const estoqueMaximoInput = document.getElementById("estoque_maximo");

let currentPage = 1;
const limit = 5;

async function loadProducts(page = 1) {

    try {

        const response = await fetch(
            `${API_URL}?page=${page}&limit=${limit}`
        );

        const products = await response.json();

        productsContainer.innerHTML = "";

        products.forEach(product => {

            const productCard = document.createElement("div");

            productCard.classList.add("product-card");

            productCard.innerHTML = `
                <h3>${product.nome}</h3>

                <p><strong>SKU:</strong> ${product.sku}</p>

                <p><strong>Preço:</strong> R$ ${product.preco_venda}</p>

                <p><strong>Quantidade:</strong> ${product.quantidade}</p>
            `;

            productsContainer.appendChild(productCard);

        });

        pageInfo.innerText = `Página ${page}`;

        currentPage = page;

    } catch (error) {

        console.error("Erro ao carregar produtos:", error);

    }

}

async function searchProducts() {
    const productName = searchInput.value.trim();

    if (productName === "") {
        loadProducts(1);
        return;
    }

    try {
        const response = await fetch(
            `${SEARCH_URL}?product_name=${encodeURIComponent(productName)}`
        );

        const products = await response.json();

        productsContainer.innerHTML = "";

        products.forEach(product => {
            const productCard = document.createElement("div");

            productCard.classList.add("product-card");

            productCard.innerHTML = `
                <h3>${product.nome}</h3>
                <p><strong>SKU:</strong> ${product.sku}</p>
                <p><strong>Preço:</strong> R$ ${product.preco_venda}</p>
                <p><strong>Quantidade:</strong> ${product.quantidade}</p>
            `;

            productsContainer.appendChild(productCard);
        });

        pageInfo.innerText = "Resultado da busca";

    } catch (error) {
        console.error("Erro ao buscar produtos:", error);
    }
}

async function createProduct(event) {
    event.preventDefault();

    const productData = {
        nome: nomeInput.value,
        sku: skuInput.value,
        codigo_barras: codigoBarrasInput.value || null,
        preco_custo: Number(precoCustoInput.value),
        preco_venda: Number(precoVendaInput.value),
        quantidade: Number(quantidadeInput.value),
        estoque_minimo: Number(estoqueMinimoInput.value),
        estoque_maximo: estoqueMaximoInput.value
            ? Number(estoqueMaximoInput.value)
            : null
    };

    try {
        const response = await fetch(PRODUCT_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(productData)
        });

        if (!response.ok) {
            const error = await response.json();
            alert(error.detail || "Erro ao cadastrar produto");
            return;
        }

        alert("Produto cadastrado com sucesso!");

        productForm.reset();

        loadProducts(1);

    } catch (error) {
        console.error("Erro ao cadastrar produto:", error);
        alert("Erro ao conectar com a API.");
    }
}

productForm.addEventListener("submit", createProduct);

searchButton.addEventListener("click", searchProducts);

searchInput.addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        searchProducts();
    }
});

prevPageButton.addEventListener("click", () => {

    if (currentPage > 1) {

        loadProducts(currentPage - 1);

    }

});

nextPageButton.addEventListener("click", () => {

    loadProducts(currentPage + 1);

});

loadProducts();