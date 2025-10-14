# Rectifex Analyzer Pro-Score (v3.0)

This repository contains the source code for the Rectifex Analyzer Pro-Score, a desktop application designed for Kubuntu that provides intelligent stock screening based on a hybrid scoring model.

## Features

- **Hybrid Scoring Model:** The application evaluates stocks based on a balanced combination of three core pillars:
    - **Quality:** Strong profitability (ROIC, etc.) and a healthy balance sheet.
    - **Valuation:** Favorable pricing (P/E, PEG ratio, etc.).
    - **Momentum:** Strong recent price performance and positive analyst revisions.
- **Sector-Specific Analysis:** The core innovation of v3.0. The application intelligently adjusts its scoring thresholds based on a stock's GICS sector, recognizing that different industries have different financial characteristics. For example, a "good" debt level for a Utility company is different from that of a Technology company.
- **Intuitive UI Controls:** The user can define their exact investment strategy by adjusting three simple sliders to weigh the importance of Quality, Valuation, and Momentum.
- **Transparent Results:** Instead of a black box, the application provides a detailed breakdown for each stock, showing which of the 12 criteria it passed or failed, including the stock's actual value and the required threshold for the given settings.
- **Asynchronous Backend:** The FastAPI backend is designed to fetch financial data for multiple tickers in parallel, significantly improving the performance of a market scan.
- **Pre-defined Market Lists:** Allows for scanning of entire market indices (e.g., S&P 500) to find top-scoring companies.

---

## Installation & Setup Guide (for Kubuntu)

This guide provides all the necessary steps to set up the development environment and build the application from source.

### 1. Install System Dependencies

First, update your system and install `git`.

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install git -y
```

### 2. Install Docker and Docker Compose

The development environment runs in containers.

```bash
# Add Docker's official GPG key:
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# Install Docker packages:
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```

### 3. Install Flatpak Tools

`flatpak` is used to package and run the final desktop application.

```bash
sudo apt install flatpak flatpak-builder -y
```

### 4. Configure Flatpak Remotes and Runtimes

Add the Flathub repository and install the necessary KDE and Node.js runtimes for building and running the app.

```bash
# Add the Flathub remote repository
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# Install the KDE Platform and SDK (Version 6.7)
flatpak install flathub org.kde.Platform//6.7 org.kde.Sdk//6.7 -y

# Install the Node.js 18 build extension for the SDK
flatpak install flathub org.freedesktop.Sdk.Extension.node18//23.08 -y
```

---

## How to Run

### 1. Clone the Repository

Clone this repository to your local machine. For example:
```bash
git clone https://github.com/BioVisualizer/Rectifex-Analyzer-Pro-Score
cd Rectifex-Analyzer-Pro-Score
```

> **Tip:** Linux file and directory names are case-sensitive. If you see an
> error such as `bash: cd: rectifex-analyzer-pro-score: No such file or
> directory`, ensure you use the exact capitalization shown above.

If you previously cloned the repository and now see
`fatal: destination path 'Rectifex-Analyzer-Pro-Score' already exists and is not
an empty directory.`, either remove the existing directory with
`rm -rf Rectifex-Analyzer-Pro-Score` (after confirming you no longer need its
contents) or reuse the existing clone by running `cd Rectifex-Analyzer-Pro-Score`.

### 2. Run the Development Environment

This command starts the backend server, the frontend dev server, and the PostgreSQL database using Docker.

```bash
docker compose up --build
```
> **Note:** The first time you run this command, the backend service may take several minutes to build as it resolves Python dependencies and creates a `poetry.lock` file. Subsequent builds will be significantly faster.

- **Frontend UI:** is available at `http://localhost:5173`
- **Backend API Docs:** are available at `http://localhost:8000/docs`

If the backend image fails to build with an error similar to `The option "--no-dev" does not exist`, your local Poetry version is newer than the one the original Dockerfile was written for. Update the `RUN poetry install` line in `backend/Dockerfile` (or pull the latest repository changes) so that it uses `poetry install --without dev --no-interaction --no-ansi`.

### 3. Build and Run the Desktop Application

To build the application as a native desktop package, use the Flatpak builder.

```bash
# Navigate to the packaging directory
cd packaging/flatpak

# Build the application
# This command reads the manifest file and builds the .flatpak file
flatpak-builder --force-clean build-dir de.rectifex.AnalyzerProScore.yml

# Install the application for the current user
flatpak-builder --user --install --force-clean build-dir de.rectifex.AnalyzerProScore.yml

# Run the installed application
flatpak run de.rectifex.AnalyzerProScore
```

> **Troubleshooting:** Building the Flatpak manifest requires live access to PyPI in order to download Python wheels such as `ujson`. If you see repeated `Temporary failure in name resolution` messages or `No matching distribution found for ujson`, verify that your network connection allows outbound HTTPS traffic from the build environment.